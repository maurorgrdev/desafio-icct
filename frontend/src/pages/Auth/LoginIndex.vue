<template>
  <q-layout view="hHh lpR fFf">
      <q-page-container>
          <q-page>
              <div class="row justify-center" style="padding-top: 20px;">
                  <q-card class="my-card" flat bordered>
                      <div class="q-pa-md" style="max-width: 400px">
                          <q-form @submit="onSubmit" @reset="onReset" class="q-gutter-md">
                              <q-input outlined v-model="login" label="Seu login *"  hint="login" />

                              <q-input outlined v-model="password" label="Sua senha *" hint="senha" />

                              <div class="row text-blue-8">
                                  <q-btn outline style=" width: 100px; color: blue-8;" label="Limpar" type="reset" class="q-ml-sm" />
                                  <q-space />
                                  <q-btn label="Entrar" style=" width: 100px;" type="submit" color="primary"/>
                              </div>
                          </q-form>
                      </div>
                  </q-card>
              </div>
          </q-page>
      </q-page-container>
  </q-layout>
</template>

<script>

import { useUsuarioStore } from 'stores/user'
import useNotify from 'src/composables/UseNotify'

export default {
  data() {
      return {
          login: '',
          password: '',
          msgError: '',
      }
  },
  setup () {
      const usuarioStore = useUsuarioStore()
      const notify = useNotify()

      return {
          usuarioStore,
          notify,
      }
  },

  methods: {
      async onSubmit ()
      {
          if(await this.validationLogin()){
              const response = await this.usuarioStore.login({
                  login: this.login,
                  senha: this.password,
              });

              if(response.status === 200){
                  this.notify.notifySuccess('Login efetuado com sucesso!');

                  this.$router.push('/users');
              } else {
                  this.notify.notifyError(this.msgError);
              }
          } else {
              this.notify.notifyError(this.msgError);
          }
      },

      async validationLogin(){
          if((this.login === '') || this.login === null || this.login.length <= 0){
              this.msgError = 'Informe um login';
              return false;
          }

          if((this.password === '') || this.password === null || this.password.length <= 0){
              this.msgError = 'Informe uma senha';
              return false;
          }

          return true;
      },

      async onReset(){
          this.login = ''
          this.password = ''
      },


  },
}
</script>

<style lang="sass" scoped>
.my-card
  width: 100%
  max-width: 350px
</style>

<!-- <style>

</style> -->

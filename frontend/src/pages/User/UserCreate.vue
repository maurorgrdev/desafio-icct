<template>
  <q-page>
      <q-card-section>
          <q-form class="q-gutter-md">
              <div class="title q-pa-md">
                  <div class="text-h6">Cadastro de Usuário</div>
                  <div class="text-subtitle2">Cadastrando novo usuário no sistema</div>
              </div>
              <div class="row">
                  <div class="q-pa-xs col-3">
                      <q-input
                          outlined
                          dense
                          v-model="dadosUsuario.nome"
                          label="Nome"
                          :rules="[
                              val => val && val.length > 0 ||
                              'Obrigatório'
                          ]"
                      />
                  </div>
                  <div class="q-pa-xs col-5">
                    <q-input
                        outlined
                        dense
                        v-model="dadosUsuario.sobrenome"
                        label="Sobrenome*"
                        :rules="[
                            val => val && val.length > 0 ||
                            'Obrigatório'
                        ]"
                    />
                  </div>
                  <div class="q-pa-xs col-4">
                    <q-input
                        outlined
                        dense
                        v-model="dadosUsuario.cpf"
                        label="CPF *"
                        :rules="[
                            val => val && val.length > 0 ||
                            'Obrigatório'
                        ]"
                        mask="###.###.###-##"
                    />
                  </div>
              </div>
              <div class="row">
                  <div class="q-pa-xs col-4">
                      <q-input
                          outlined
                          dense
                          type="email"
                          v-model="dadosUsuario.email"
                          label="Email *"
                          :rules="[
                              val => val && val.length > 0 ||
                              'Obrigatório'
                          ]"
                      />
                  </div>
                  <div class="q-pa-xs col-4">
                    <q-input
                        outlined
                        dense
                        v-model="dadosUsuario.login"
                        label="Login*"
                        :rules="[
                            val => val && val.length > 0 ||
                            'Obrigatório'
                        ]"
                    />
                  </div>
                  <div class="q-pa-xs col-4">
                    <q-input
                        outlined
                        dense
                        v-model="dadosUsuario.senha"
                        label="Senha de acesso*"
                        :rules="[
                            val => val && val.length > 0 ||
                            'Obrigatório'
                        ]"
                        :type="isPwdPrincipal ? 'senha' : 'text'"
                    >
                        <template v-slot:append>
                            <q-icon
                            :name="isPwdPrincipal ? 'visibility_off' : 'visibility'"
                            class="cursor-pointer"
                            @click="isPwdPrincipal = !isPwdPrincipal"
                            />
                        </template>
                    </q-input>
                </div>
              </div>
          </q-form>
      </q-card-section>

      <q-card-actions class="row text-blue-5" style="padding-left: 25px; padding-right: 25px;">
          <q-space />
          <q-btn @click="clickCancel" outline style=" width: 150px;" label="Cancelar" />
          <q-btn @click="clickSubmit" style=" width: 150px;" color="blue-5" label="Salvar" />
        </q-card-actions>
  </q-page>
</template>

<script>
import { useUsuarioStore } from 'src/stores/user';

export default {
  setup(){
      const usuarioStore = useUsuarioStore()

      return {
          usuarioStore,
      }
  },

  data() {
      return {
          messageError: '',

          dadosUsuario: {
              nome: '',
              cpf: '',
              email: '',
              sobrenome: '',
              senha: '',
              login: ''
          },

          isPwdPrincipal: true,
          isPwdSecundario: true,
      }
  },

  methods: {

      clickCancel(){
          this.$router.push('/users')
      },

      async clickSubmit(){
          if(await this.validarFormulario_NovoUsuario()){
              let response = await this.usuarioStore.create(this.dadosUsuario)

              if(response.status === 201 || response.status === 200){
                  this.$router.push('/users')
              } else {
                  alert(response.data.message)
              }
          } else {
              alert(this.messageError)
          }
      },

      // Validar campos preenchidos pelo usuário
      validarFormulario_NovoUsuario(){
          if((this.dadosUsuario.nome === '') || this.dadosUsuario.nome === null || this.dadosUsuario.nome.length <= 0){
              this.messageError = 'Informe uma nome válido';
              return false;
          }

          if((this.dadosUsuario.cpf === '') || this.dadosUsuario.cpf === null || this.dadosUsuario.cpf.length <= 0){
              this.messageError = 'Informe uma cpf válido';
              return false;
          }

          if((this.dadosUsuario.sobrenome === '') || this.dadosUsuario.sobrenome === null || this.dadosUsuario.sobrenome.length <= 0){
              this.messageError = 'Informe uma sobrenome válido';
              return false;
          }

          if((this.dadosUsuario.email === '') || this.dadosUsuario.email === null || this.dadosUsuario.email.length <= 0){
              this.messageError = 'Informe um e-mail válido';
              return false;
          }

          if((this.dadosUsuario.senha === '') || this.dadosUsuario.senha === null || this.dadosUsuario.senha.length <= 0 ){
              this.messageError = 'Informe uma senha';
              return false;
          }

          if((this.dadosUsuario.login === '') || this.dadosUsuario.login === null || this.dadosUsuario.senha.login <= 0 ){
              this.messageError = 'Informe uma login válido';
              return false;
          }


          return true;
      },
  }
}

</script>

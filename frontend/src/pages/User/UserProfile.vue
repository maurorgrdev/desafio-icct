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
                          disable
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
                        disable
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
                        disable
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
                          disable
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
                        disable
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
                        disable
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

      <q-card-actions class="row text-blue-10" style="padding-left: 25px; padding-right: 25px;">
          <q-space />
          <q-btn @click="clickCancel" outline style=" width: 150px;" label="Voltar" />
        </q-card-actions>
  </q-page>
</template>

<script>
import { useUsuarioStore } from 'src/stores/user';

export default {
  props: ['usuario_id'],


  setup(){
    const usuarioStore = useUsuarioStore()

    return {
        usuarioStore,
    }
  },

  async mounted() {
    await this.usuarioStore.loadUsuario(this.usuario_id);

    this.dadosUsuario = {...this.usuarioStore.getUsuario}
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
  }
}

</script>

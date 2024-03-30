<template>
  <q-page>

      <q-dialog v-model="showDialogDeleteUsuario" persistent>
          <q-card
            style="width: 550px; max-width: 80vw;"
          >
              <q-card-section>
                  <h6>O usuário - {{ usuario_delete.nome }} -   será excluído. Confirmar ação?</h6>
              </q-card-section>
              <q-card-actions class="row text-blue-5">
                  <q-space />
                  <q-btn @click="showDialogDeleteUsuario = false" outline style=" width: 150px;" label="VOLTAR" />
                  <q-btn @click="confirmDeleteUsuario" style=" width: 150px;" color="blue-5" label="Confirmar" />
              </q-card-actions>
          </q-card>
      </q-dialog>



      <div class="q-pa-xl">
          <q-table
          flat
              :rows="usuarioStore.getUsuarios"
              :columns="columns"
              row-key="id"
              table-header-class="bg-blue-5 text-white"
          >
              <template v-slot:body="props">
                  <q-tr :props="props">
                      <q-td key="id" :props="props">
                          {{ props.row.id }}
                      </q-td>
                      <q-td key="nome" :props="props">
                          {{ props.row.nome }}
                      </q-td>
                      <q-td key="email" :props="props">
                          {{ props.row.email }}
                      </q-td>
                      <q-td key="actions" :props="props">
                          <q-btn color="blue-5" class="q-mr-md" size="sm" round icon="mode_edit" @click="$router.push(`/users/edit/${props.row.id}`)"><q-tooltip> Editar Usuário </q-tooltip></q-btn>
                          <q-btn color="blue-5" class="q-mr-md" size="sm" round icon="visibility" @click="$router.push(`/users/profile/${props.row.id}`)"><q-tooltip> Visualizar Usuário </q-tooltip></q-btn>
                          <q-btn color="blue-5" class="q-mr-md" size="sm" round icon="delete" @click="openDialogDeleteUsuario(props.row)"><q-tooltip> Deletar Usuário </q-tooltip></q-btn>

                      </q-td>
                  </q-tr>
              </template>
              <template v-slot:top>
                  <div class="title q-py-xl">
                      <div class="text-h5">Usuários</div>
                      <div class="text-subtitle2">Usuários cadastrados no sistema</div>
                  </div>
                  <q-space />
                  <q-btn color="blue-5" label="NOVO USUÁRIO"  @click="$router.push('/users/create')"/>
              </template>
          </q-table>
      </div>
  </q-page>
</template>

<script>
import {useUsuarioStore} from 'src/stores/user'

export default {
  setup() {
      const usuarioStore = useUsuarioStore()

      return {
          usuarioStore,
      }
  },

  data() {
      return {
          showDialogListaEndereco: false,
          showDialogNovoEndereco: false,
          showDialogDeleteEndereco: false,
          showDialogDeleteUsuario: false,
          showDialogVisualizaEndereco: false,

          user_enderecos: {},

          novo_endereco: {
              cep: '',
              logradouro: '',
              tipo: '',
              bairro: '',
              numero: '',
              complemento: '',
              localidade: '',
              uf: '',
          },

          columns: [
              {
                  name: 'id',
                  label: 'Código',
                  align: 'center',
                  field: 'Código',
                  sortable: true
              },
              { name: 'nome', align: 'center', label: 'Nome', field: 'nome', sortable: true },
              { name: 'email', align: 'center', label: 'Email', field: 'email', sortable: true },
              { name: 'actions', align: 'center', label: 'Ações'},
          ],

          columnsEndereco: [
              { name: 'tipo', align: 'center', label: 'Tipo endereço', field: 'tipo', sortable: true },
              { name: 'cep', align: 'center', label: 'CEP', field: 'cep', sortable: true },
              { name: 'logradouro', align: 'center', label: 'Dados endereço', field: 'logradouro', sortable: true },
              { name: 'actions', align: 'center', label: 'Ações'},
          ],

          endereco_delete: {},

          usuario_delete: {},

          messageError: '',

          endereco_visualizado: {},
      }
  },

  async mounted(){
      await this.usuarioStore.loadUsuarios();
  },

  methods: {
      openDialogDeleteUsuario(usuario){
          this.usuario_delete = {...usuario}

          this.showDialogDeleteUsuario = true
      },

      async confirmDeleteUsuario(){
          const response = await this.usuarioStore.delete(this.usuario_delete.id);

          if(response.status == 201 || response.status == 200){
              await this.usuarioStore.loadUsuarios();

              this.showDialogDeleteUsuario = false
          } else {
              alert('Error ao excluir endereço')
          }
      },
  }
}

</script>

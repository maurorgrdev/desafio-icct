import { defineStore } from 'pinia'
import { api } from 'boot/axios'

export const useUsuarioStore = defineStore("usuario", {
    state: () => ({
        usuario: {},
        usuarios: [],
    }),

    getters: {
        getUsuario(state){
            let copyUsuario = state.usuario

            return {
                ...copyUsuario
            }
        },

        getUsuarios(state){
            let copyUsuarios = state.usuarios.map((usuario) => {
                return {
                    ...usuario
                }
            })

           return copyUsuarios
        },
    },

    actions: {
        async loadUsuarios(){
            try {
                const result = await api.get('/users/')

                this.usuarios = result.data.users
            } catch (error) {
                alert(error)
            }
        },

        async loadUsuario(id){
            try {
                const result = await api.get(`/users/${id}`)

                this.usuario = result.data.user
            } catch (error) {
                alert(error)
            }
        },

        async create(data){
            try {

                const request = {
                    ...data
                }
                const response = await api.post(`/users/`, request)

                console.log(response.data)
                return response
            } catch (error) {
                return error.response
            }
        },

        async update(data){
            try {

                const request = {
                    ...data
                }

                const response = await api.put(`/users/${data.id}`, request)

                return response.data
            } catch (error) {
                return error.response
            }
        },

        async delete(id){
            try {
                const result = await api.delete(`/users/${id}`)

                return result
            } catch (error) {
                return error.response
            }
        },

        async login(data){
          try {
              const response = await api.post('/authentic/login', data);

              this.usuario = response.data.user;

              await localStorage.setItem("token", response.data.token);

              return response;
          } catch (error) {
              localStorage.setItem("token", '');
              this.usuario = {};

              return error.response;
          }
      },
    }

  });

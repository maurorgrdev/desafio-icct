import { useQuasar } from 'quasar'

export default function useNotify (){
    const $q = useQuasar();

    const notifySuccess = (message) => {
        $q.notify({
            type: 'positive',
            message: message ? message : 'Registro feito com sucesso.'
          })
    }

    const notifyError = (message) => {
        $q.notify({
            type: 'negative',
            message: message ? message : 'Erro na requisição.'
          })
    }

    return {
        notifyError,
        notifySuccess
    }
}

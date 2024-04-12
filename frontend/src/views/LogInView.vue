<script lang="ts">
import axios from 'axios'
import InputText from './../components/InputText.vue'
export default{
    name:'SignUp',
    components: {
        InputText
    },
    data() {
        return {
            username: '',
            password: '',
            isError: false,
            errorMessage: '',
            isOk: false,
            okMessage: ''
        };
    },
    methods: {
        submitForm(e) {
            axios.defaults.headers.common['Authorization'] = ''
            localStorage.removeItem('access')

            const formData={
                username: this.username,
                password: this.password
            }
            axios
                .post('/api/v1/login/', formData)
                .then(response=>{
                    console.log(response)


                })
                .catch(error=>{
                    console.log(error)
                })
        }
    }

}
</script>
<template>
    <div>
        <h1>Log In</h1>
        <form @submit.prevent="submitForm">

            <InputText label="Nombre de usuario" v-model="username" required inputId="username"
                :placeholder="'Introduce tu nombre de usuario'" :isError="isError" :errorMessage="errorMessage"
                :isOk="isOk" :okMessage="okMessage" />

            <InputText label="Passwword" v-model="password" required inputId="username"
                :placeholder="'Introduce tu contraseña'" :isError="isError" :errorMessage="errorMessage" :isOk="isOk"
                :okMessage="okMessage" />

            <button type="submit">Iniciar sesión</button>
        </form>
        <p>¿No tienes una cuenta? <router-link to="/register">Registrarse</router-link></p>
    </div>
</template>


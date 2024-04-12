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
            const formData={
                username: this.username,
                password: this.password
            }
            axios
                .post('/api/v1/register/', formData)
                .then(response=>{
                    console.log(response)
                    this.$router.push('/')

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
        <h1>Sign Up</h1>
        <form @submit.prevent="submitForm">

<InputText label="Nombre de usuario" v-model="username" required inputId="username"
    :placeholder="'Introduce tu nombre de usuario'" :isError="isError" :errorMessage="errorMessage"
    :isOk="isOk" :okMessage="okMessage" />

<InputText label="Password" v-model="password" required inputId="username"
    :placeholder="'Introduce tu contraseña'" :isError="isError" :errorMessage="errorMessage" :isOk="isOk"
    :okMessage="okMessage" />

<button type="submit">Sign Up</button>
</form>
    </div>
</template>

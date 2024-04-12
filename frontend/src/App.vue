<script lang="ts">
import HeaderTitle from '@/components/HeaderTitle'
import axios from 'axios'

export default{
  name:'App',
  beforeCreate(){
    this.$store.commit("initializaStore")
    const access = this.$store.state.access

    if(access){
      axios.defaults.headers.common['Authorization']= "JWT" + access
    }else{
      axios.defaults.headers.common['Authorization'] = ''
    }

  }
}

</script>

<template>
<div id="app">
<HeaderTitle />
<div id="nav">
  <router-link to="/">Home</router-link>
  <router-link to="/login">Login</router-link>
  <router-link to="/signup">Signup</router-link>
</div>
  <router-view />
</div>
</template>
<style >
#app{
  color: black;
  text-align: center;
}
#nav{
  display: inline-flex;
  width: 80%;
  justify-content: space-around;
  padding: 30px;
  a{
    font-weight: bold;
    color: black;
  }
  .router-link-active.router-link-exact-active{
      color: purple;
    }
}
</style>


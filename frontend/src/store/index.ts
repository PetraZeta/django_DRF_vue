
import {createStore} from 'vuex';

 export default createStore({
    state:{
        access:'',
        refresh:''
    },
    mutacions:{
        initializeStore(state){
            if(localStorage.getItem('access')){
                state.access= localStorage.getItem('access') || '';
            }else{
                state.access='';
            }
        },
        setAccess(state,access){
            state.access=access
        },
     
        
    },
    actions:{

    },
    modules:{

    }

 });
<script lang="ts">
import axios from 'axios'
import ItemList from './../components/ItemList.vue'
import { Worker } from '../models/worker.model';

export default {
    name: 'Home',
    components: {
        ItemList
    },
    data() {
        return {
            workers: [] as Worker[] 
        };
    },
    created() {
        this.fetchWorkers();
    },
    methods: {
        async fetchWorkers() {
            try {
                const response = await axios.get('/api/v1/worker');
                this.workers = response.data; 
                console.log(response.data)
            } catch (error) {
                console.error('Error al obtener los trabajadores:', error);
            }
        }
    }
}
</script>
<template>
    <div>
        <h1>Inicio</h1>
        <ItemList :workers="workers" />
    </div>
   
</template>

<script setup lang="ts">
import {   ref } from 'vue';
import { Worker } from '../models/worker.model'

/* const { workers } = defineProps<{
    workers: Worker[];
}>(); 
 */
const selectedWorker = ref<Worker | null>(null);

const showDetail = (worker: Worker) => {
    selectedWorker.value = worker;
    console.log(worker)
};


</script>

<template>

    <li v-for="worker in workers" :key="worker.name_first" @click="showDetail(worker)"
        class="flex justify-between gap-x-6 py-5 cursor-pointer">
        <div class="flex min-w-0 gap-x-4">
            <img src="https://unsplash.com/es/s/fotos/random-person" :alt="worker.name_first"
                class="h-12 w-12 flex-none rounded-full bg-gray-50" />
            <div class="min-w-0 flex-auto">
                <p class="text-sm font-semibold leading-6 text-gray-900">{{ worker.name_first }} {{ worker.name_last }}</p>
             <!--    <p class="mt-1 truncate text-xs leading-5 text-gray-500">{{ worker.email }}</p> -->
            </div>
        </div>
        <div class="hidden shrink-0 sm:flex sm:flex-col sm:items-end">
            <p class="text-sm leading-6 text-gray-900">{{ worker.gender }}</p>
         <!--    <p class="mt-1 text-xs leading-5 text-gray-500">Birthday <time >{{ formatDate(worker.dob.date) }}</time></p> -->
        </div>
        
    </li>

</template>
<script setup lang="ts">
import { ref   } from 'vue';
import { Worker } from "../models/worker.model";
import UserModal from './UserModal.vue'


const workers = ref<Worker[]>([]);

const selectedUser = ref<Worker | null>(null);
const isModalOpen = ref(false);


const showDetail = (worker: Worker) => {
    selectedUser.value = worker;
    isModalOpen.value = true;
    console.log(worker)
    console.log(isModalOpen.value)

};
const closeModal = () => {
    selectedUser.value = null;
};

</script>

<template>
    <section class="container mx-auto rounded-md shadow-md">
        <ul role="list" class="divide-y divide-gray-100 px-5">
            <li v-for="worker in workers" :key="worker.id" @click="showDetail(worker)"
                class="flex justify-between gap-x-6 py-5 cursor-pointer">
                <div class="flex min-w-0 gap-x-4">
             <!--        <img :src="worker.picture" :alt="worker.name_first"
                        class="h-12 w-12 flex-none rounded-full bg-gray-50" /> -->
                    <div class="min-w-0 flex-auto">
                        <p class="text-sm font-semibold leading-6 text-gray-900">{{ worker.name_first }} {{ worker.name_last
                            }}</p>
                        <p class="truncate text-xs leading-5 text-gray-500">{{ worker.email }}</p>
                    </div>
                </div>
                <div class="hidden shrink-0 sm:flex sm:flex-col sm:items-end">
                    <p class="text-sm leading-6 text-gray-900">{{ worker.gender }}</p>
               <!--      <p class="text-xs leading-5  text-gray-900 ">Registered: <span> <time class=" text-gray-500">{{
                formatDate(worker.registered.date) }}</time></span></p> -->
                </div>

            </li>
        </ul>

    </section>

    <UserModal :worker="selectedUser" v-if="selectedUser !== null" :onClose="closeModal" />

</template>
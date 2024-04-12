<script setup lang="ts">
import { defineProps } from 'vue';
import { Worker } from "../models/worker.model";


interface Props {
  worker: Worker | null;
}

defineProps<Props>();
const emits = defineEmits();
const closeModal = () => {
  emits('close');
};

</script>
<template>
  <div v-if="worker" class="relative z-10" aria-labelledby="modal-title" role="dialog" aria-modal="true">

    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"></div>

    <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
      <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">

        <div
          class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
          <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
            <div class="sm:flex sm:items-start">
              <div
                class="mx-auto flex h-32 w-32 flex-shrink-0 items-center justify-center rounded-full bg-red-100 sm:mx-0 sm:h-15 sm:w-15">
           <!--      <img :src="worker.picture.large" :alt="worker.name.first"
                  class="h-32 w-32 flex-none rounded-full bg-gray-50" /> -->

              </div>
              <div class="min-w-0 mt-5 flex-auto">

                <h2 class="text-xl font-semibold text-center leading-6 text-gray-900" id="modal-title"> {{
      worker.name_first }} {{
        worker.name_last }}</h2>
              <p class="mt-1 truncate text-sm text-center leading-5 text-gray-500">{{ worker.email }}</p>
                <p class="mt-3 text-xs leading-5 text-center text-gray-900 ">Job: <span
                    class="mx-5 text-gray-500"><time>{{worker.work}}</time></span> </p> 
              </div>
            </div>
          </div>
          <div class="m-3 text-center sm:ml-4 sm:mt-0 sm:mx-5 sm:text-center">


            <div
              class="mt-2 px-4 pb-4 sm:p-6 sm:pb-4 border-t  border-gray-200 pt-5 py-1 sm:flex justify-between space-x-4">
              <div class="flex justify-around items-center">
                <svg class="h-8 w-8 text-black-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                </svg>

              </div>
              <div class="flex-col sm:flex sm:flex-auto  justify-between space-x-4">
<!--                 <p class="text-sm text-black-500">{{ user.location.city }}, {{ user.location.state }}, <span
                    class="text-xs text-gray-500">{{ user.location.state }}</span></p>
                <p class="text-sm text-gray-500"> <span class="text-sm text-gray-500">({{ user.location.postcode }})
                    {{ user.location.street.name }}, {{ user.location.street.number }}</span></p>
                <a class="text-xs bold underline text-right text-gray-700"
                  :href="'https://www.google.com/maps?q=' + user.location.coordinates.latitude + ',' + user.location.coordinates.longitude"
                  target="_blank">View Map</a> -->
              </div>
            </div>
          </div>
          <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">

            <button @click="closeModal" type="button"
              class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto">Cerrar</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<template>
  <MainView />
</template>


<script>

import { initFlowbite } from 'flowbite'
import MainView from './components/StudyView.vue'  


export default {
  name: 'App',
  components : {
    MainView
  }, 
  mounted() {
        initFlowbite();
    }, 
}
</script>

<style>
@import "./assets/css/font.css";
@import "./assets/css/styling.css";
</style>



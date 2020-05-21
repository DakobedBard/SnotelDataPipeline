<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/baker.jpg"> -->
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <MountainComponent name = "Bonanza Peak" />
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import MountainComponent from './components/Mountain.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
    MountainComponent
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

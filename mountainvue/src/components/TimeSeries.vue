

<template>
  <div class="moutain">
    <h1>{{ name }}</h1>
    {{ attributeA }}
     <!-- <a @click="getLocations('bro')">Click me!</a> -->
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'TimeSeriesComponent',
  props: {
    name: String
  },
  data: function() {
		return {
            cars : ["Saab", "Volvo", "BMW"],
            attributeA: 'valueA',
            locations: []
		};
	}
    ,
  methods: {
        getLocations: function (text){
            console.log("You suck! " + text + " " + this.name )  
            axios.get('http://localhost:8081/data/location/')
                .then(response => {this.locations = response.data})
                .catch((error) => console.log(error))
            console.log("The number of cars is " + this.locations.length)
        }
    }
  }
</script>




<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>

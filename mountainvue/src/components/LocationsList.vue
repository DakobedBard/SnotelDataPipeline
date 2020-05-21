

<template>
  <div class="locations">
    <v-simple-table height="300px">
    <template v-slot:default>
    <thead>
        <tr>
          <th class="text-left">Location</th>
          <th class="text-left">Elevation</th>
          <th class="text-left">Region</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="car in cars" :key="car.name">
          <td>{{ car }}</td>
          <td>{{ car }}</td>
          <td> Wenatchee </td>
        </tr>
      </tbody>
    </template>
    </v-simple-table>
  </div>
</template>


      <!-- <v-simple-table height="300px">
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-left">Name</th>
          <th class="text-left">Calories</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in desserts" :key="item.name">
          <td>{{ item.name }}</td>
          <td>{{ item.calories }}</td>
        </tr>
      </tbody>
    </template>
  </v-simple-table> -->
      <!-- whad
    <ul id="example-1">
        <li v-for="car in cars" :key="car.name">
            {{ car }} 
        </li>
    </ul>
    <a @click="getLocations('bro')">Click me!</a>
    <ul id="locations">
        <li v-for="location in locations" :key="location.location_id">
            
            {{ location.location_name }} \n
        </li>
    </ul> -->




<script>
import axios from 'axios'
export default {
  name: 'LocationsList',
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

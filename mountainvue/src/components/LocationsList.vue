

<template>
  <div class="locations">
    
    <v-simple-table dark>
    
    <template v-slot:default>
    <thead style="height:1000px">
        <tr>
          <th class="text-left">Location</th>
          <th class="text-left">Elevation</th>
          <th class="text-left">Region</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="location in locations" :key="location.location_id">
          <td>{{ location.location_name }}</td>
          <td> {{ location.elevation  }} </td>
          <td> Wenatchee </td>
        </tr>
      </tbody>
    </template>
    </v-simple-table>
  </div>

</template>



<script>
import axios from 'axios'
export default {
  name: 'LocationsList',
  created(){
    this.locationRequest()
  },

  data: function() {
    var location_array = [];
    axios.get('http://localhost:8081/data/location/')
                .then(response => {location_array = response.data})
                .catch((error) => console.log(error))
    
    console.log("Locations " + location_array.length)
    
    return {
            search: '',
            headers: [
          {
            text: 'Dessert (100g serving)',
            align: 'start',
            sortable: false,
            value: 'name',
          }],
          desserts: [
            {
              name: 'Frozen Yogurt',
              calories: 159,
              fat: 6.0,
              carbs: 24,
              protein: 4.0,
              iron: '1%',
            },
            {
              name: 'Ice cream sandwich',
              calories: 237,
              fat: 9.0,
              carbs: 37,
              protein: 4.3,
              iron: '1%',
            }],

            cars : ["Saab", "Volvo", "BMW"],
            attributeA: 'valueA',
            locations: []
		};
	}
    ,
  methods: {
        locationRequest: function(){
          axios.get('http://localhost:8081/data/location/')
                .then(response => {this.locations = response.data})
                .catch((error) => console.log(error))
        },

        getLocations: function (text){
            console.log("You suck! " + text + " " + this.name )  
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

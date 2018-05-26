<template>
  <details id="newPrescContainer" class="container detailsContainer boxshadow boxborder">
    <summary class="detailsSummary textBig">База ліків</summary>
    <div class="detailsContent">
      <input name="medSearchTerm" type="text" title="Пошук препаратів"
             v-bind:placeholder="search_by_name ? 'Пошук за назвою' : 'Пошук за вмістом'" v-on:change="find_med('a')"
             class="textInput textMedium boxborder boxshadow" style="width: calc(100% - 86px); margin-bottom: 10px">
      <label class="switch">
        <input type="checkbox" @click="swap_placeholder()">
        <span class="sliderSwitch boxshadow"></span>
      </label>

      <hr>

      <p id="foundMeds">{{found_meds}}</p>

    </div>
  </details>
</template>

<script>
export default {
  name: 'MedsDB',
  methods: {
    swap_placeholder: function () {
      this.search_by_name = !this.search_by_name
    },
    find_med: function (med) {
      console.log('asd')
      this.$http.post('http://10.10.225.248:5000/search_name').then((response) => {
        console.log(response.data)
      }, response => {
        console.log('request error')
      })
    }
  },
  data: function () {
    return {
      search_by_name: true,
      found_meds: 'asd'
    }
  }
}
</script>

<style scoped>
  p {
    margin-top: 0;
    margin-left: 16px;
  }

  ::-webkit-scrollbar {
    display: none;
  }

</style>

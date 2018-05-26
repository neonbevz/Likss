<template>
  <details id="newPrescContainer" class="container detailsContainer boxshadow boxborder">
    <summary class="detailsSummary textBig">Новий рецепт</summary>
    <div class="detailsContent">
      <input name="medSearchTerm" type="text" title="Пошук препарату"
             v-bind:placeholder="search_by_name ? 'Пошук за назвою' : 'Пошук за вмістом'"
             class="textInput textMedium boxborder boxshadow" style="width: calc(100% - 86px); margin-bottom: 10px">
      <label class="switch">
        <input type="checkbox" @click="swap_placeholder()">
        <span class="sliderSwitch boxshadow"></span>
      </label>

      <hr>
      <p class="textSmall">Дозування</p>
      <input type="radio" name="doze" value="1" checked>1<br>
      <input type="radio" name="doze" value="2">2<br>
      <input type="radio" name="doze" value="2">3<br>

      <a href="https://codersblock.com/blog/checkbox-trickery-with-css/">Some custom radios here</a>

      <hr>
      <p class="textSmall">Частота прийому</p>

      <input type="number" name="frequency" min="1" max="15" value="1">
      <input type="range" name="days" min="0" max="90">
      <a href="https://codepen.io/trevanhetzel/pen/rOVrGK">Custom slider and droplist</a>

      <div class="buttonCircle buttonPlus boxshadow">+</div>

    </div>
  </details>
</template>

<script>
export default {
  name: 'NewPrescription',
  methods: {
    swap_placeholder: function () {
      this.search_by_name = !this.search_by_name
    }
  },
  data: function () {
    return {
      search_by_name: true
    }
  }
}
</script>

<style scoped>
details {
  /*background: linear-gradient(to bottom right, #cfd9dfCC, #e2ebf0CC);*/
  background: rgba(255, 255, 255, 0.7);
}
p {
  margin-top: 0;
  margin-left: 16px;
}

::-webkit-scrollbar {
  display: none;
}

.buttonPlus {
  margin: 0 20px 20px 0;
  float: right;
  bottom: 0;
  background: linear-gradient(to bottom right, #F9A007, #F25C05);
}
</style>

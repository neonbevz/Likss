<template>
  <details id="newPrescContainer" class="container detailsContainer boxshadow boxborder">
    <summary class="detailsSummary textBig">Історія рецептів</summary>
    <div class="detailsContent">
      <input name="medSearchTerm" type="text" title="Пошук рецептів" placeholder="Пошук за іменем"
             class="textInput textMedium boxborder boxshadow" style="width: calc(100% - 86px); margin-bottom: 10px">
      <label class="switch">
        <input type="checkbox">
        <span class="sliderSwitch boxshadow"></span>
      </label>

      <div class="historyBlock">
        <p class="textBig">Петроцилін</p>
        <button class="boxborder boxshadow">Перевірити ім'я</button>
        <p class="textMedium">15мг, 2 рази на день</p>
        <time class="textBig">2018-05-20 23:23</time>
      </div>
      <div class="historyBlock">
        <p class="textBig">Петродиклак</p>
        <button class="boxborder boxshadow">Перевірити ім'я</button>
        <p class="textMedium">50мг, 3 рази на тиждень</p>
        <time class="textBig">2018-05-19 16:12</time>
      </div>
      <div class="historyBlock">
        <p class="textBig">Петро гель</p>
        <button class="boxborder boxshadow">Перевірити ім'я</button>
        <p class="textMedium">20мг, 1 раз на день</p>
        <time class="textBig">2018-05-19 15:14</time>
      </div>
    </div>
  </details>
</template>

<script>
export default {
  name: 'NewPrescription'
}
</script>

<style scoped>
p {
  margin-top: 0;
  margin-left: 16px;
}

.historyBlock {
  width: 100%;
  padding: 5px;
  margin: 0;
  border-top: 1px solid rgba(0, 0, 0, 0.5);
  overflow: auto;
}
.historyBlock p {
  float: left;
  margin: 5px;
}
.historyBlock time {
  float: right;
  margin: 5px;
}
.historyBlock button {
  float: right;
  margin: 10px;
  outline: none;
}
/* Remove the scrollbar */
::-webkit-scrollbar {
  display: none;
}
</style>

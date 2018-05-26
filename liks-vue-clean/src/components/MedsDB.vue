<template>
  <details id="newPrescContainer" class="container detailsContainer boxshadow boxborder">
    <summary class="detailsSummary textBig">База ліків</summary>
    <div class="detailsContent">
      <input name="medSearchTerm" type="text" title="Пошук препарату" placeholder="Пошук за назвою"
             class="textInput textMedium boxborder boxshadow" style="width: calc(100% - 86px); margin-bottom: 10px">
      <label class="switch">
        <input type="checkbox">
        <span class="sliderSwitch boxshadow"></span>
      </label>

      <hr>

    </div>
  </details>
</template>

<script>
export default {
  name: 'MedsDB'
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

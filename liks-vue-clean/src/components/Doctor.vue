<template>
  <div id="doctorContainer" class="container boxshadow boxborder">
    <div class="gradientContainer boxshadow">
      <img :src="doctorProfilePictureSrc" id="doctorProfilePicture"/>
    </div>
    <p id="doctorSurname" class="textBig doctorText">{{ doctorSurname }}</p>
    <p id="doctorName" class="textMedium doctorText">{{ doctorName }}</p>
    <p id="doctorPosition" class="textSmall doctorText">{{ doctorPosition }}</p>
    <p id="doctorHospital" class="textSmall doctorText">{{ doctorHospital }}</p>
  </div>
</template>

<script>
export default {
  name: 'Doctor',
  data () {
    return {
      doctorProfilePictureSrc: '/static/profile_blank.jpg',
      doctorSurname: 'Петров',
      doctorName: 'Петро Петрович',
      doctorPosition: 'Лікуючий лікар',
      doctorHospital: 'Петрівська лікарня #1'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#doctorContainer {
  text-align: right;
  /*background-color: #5ee7dfB3;*/
  background: linear-gradient(to bottom right, #485563CC, #29323cCC);
  /*background-color: rgb(130, 130, 130);*/
  color: white;
}
.gradientContainer {
  width: 30%;
  max-width: 98px;
  height: auto;
  padding: 0;
  position: relative;
  float: left;
  margin: 10px;
  border-radius: 50%;
  background: linear-gradient(to bottom right, #D80CE8, #A700FF, #600CE8);
  overflow: auto;
}
.gradientContainer:before{
  content: "";
  display: block;
  padding-top: 100%;
}
#doctorProfilePicture {
  position: absolute;
  top: 0;
  left: 0;
  width: calc(100% - 2px);
  margin: 1px;
  border-radius: 50%;
}
.doctorText {
  margin: 10px;
}
</style>

<template>
  <div id="app">
    <Header/>
    <Doctor/>
    <NewPrescription/>
    <History/>
    <MedsDB/>
  </div>
</template>

<script>
import Header from './components/Header'
import Doctor from './components/Doctor'
import NewPrescription from './components/NewPrescription'
import History from './components/History'
import MedsDB from './components/MedsDB'

export default {
  name: 'App',
  components: {
    Header,
    NewPrescription,
    Doctor,
    History,
    MedsDB
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Open+Sans');
html {
  background-image: url('/static/gradientbg.jpg');
  background-size: cover;
  background-attachment: fixed;
  /*background: linear-gradient(to bottom left, #09203f 0%, #537895 100%);*/
  /*background: linear-gradient(to bottom right, #D80CE899, #A700FF99, #600CE899) fixed;*/
  /*background-color: rgb(200, 200, 200);*/
}
body { margin: 0; }
#app {
  width: 100%;
  padding: 0;
  /*margin: 60px 0 0;*/
  margin: 0;
  font-family: 'Open Sans', sans-serif;
  letter-spacing: 1px;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.container {
  width: 90%;
  max-width: 500px;
  margin: 10px;
  padding: 5px;
  overflow: auto;
  background-color: white;
}
@keyframes invisiblyGrowFontSize {
  0% {
    font-size: 0;
    opacity: 0;
  }
  100% {
    font-size: 1em;
    opacity: 0;
  }
}
@keyframes fadeIn {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}
.detailsContainer {
  transition: max-height 0.7s ease-out;
  transform-origin: top;
  text-align: left;
  overflow-x: hidden;
  overflow-y: scroll;
}
.detailsContainer:not([open]) {
  max-height: 100px;
}
.detailsContainer[open] {
  max-height: 600px;
}
.detailsContainer[open] .detailsContent {
  animation-name: invisiblyGrowFontSize, fadeIn;
  animation-duration: 700ms, 500ms;
  animation-delay: 0ms, 200ms;
}
.detailsSummary {
  margin: 5px;
  outline:none;
}
.boxshadow {
  box-shadow: 2px 2px 2px grey;
}
.boxborder {
  border-radius: 10px;
  border: 1px solid rgba(0, 0, 0, 0.1);
}
.textBig {
  font-size: 20px;
  font-weight: bolder;
}
.textMedium {
  font-size: 18px;
  font-weight: normal;
}
.textSmall {
  font-size: 15px;
  font-weight: normal;
}
.textInput {
  margin: 5px;
  padding: 3px;
  padding-left: 8px;
  float: left;
  outline: none;
  background-color: rgba(0, 0, 0, 0.1);

}
.switch {
  position: relative;
  /*display: inline-block;*/
  float: right;
  width: 50px;
  height: 27px;
  margin: 6.5px;
}
.switch input {display:none;}
.sliderSwitch {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  border-radius: 27px;
  background-color: rgba(0, 0, 0, 0.1);
  -webkit-transition: .4s;
  transition: .4s;
}

.sliderSwitch:before {
  position: absolute;
  content: "";
  height: 23px;
  width: 23px;
  left: 2px;
  bottom: 2px;
  border-radius: 50%;
  background-color: white;
  -webkit-transition: .4s;
  transition: .4s;
}

input:checked + .sliderSwitch {
  background-color: #2196F3;
}

input:focus + .sliderSwitch {
  box-shadow: 0 0 1px #2196F3;
}

input:checked + .sliderSwitch:before {
  -webkit-transform: translateX(23px);
  -ms-transform: translateX(23px);
  transform: translateX(23px);
}
hr {
  width: 100%;
  color: rgba(0, 0, 0, 0.5);
}
.buttonCircle {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  text-align: center;
  vertical-align: middle;
  line-height: 50px;
  color: white;
  font-size: 45px;
}

</style>

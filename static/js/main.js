// Script for Materialize elements - modal, navbar and tooltips

$(document).ready(function() {
     $('.modal').modal();
     $(".button-collapse").sideNav();
     $('.tooltipped').tooltip();
     $('.select').material_select();
    });

function goBack() {
  window.history.back();
};
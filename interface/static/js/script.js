/**
 * @Author: Jason Y. Wu
 * @Date:   2023-07-18 15:41:04
 * @Last Modified by:   Jason Y. Wu
 * @Last Modified time: 2023-07-18 15:41:13
 */
'use strict';
function submitForm() {
    var submitBtn = document.getElementById('submitBtn');
    var loadingSpinner = document.getElementById('loadingSpinner');
    var myForm = document.getElementById('myForm');
    // Disable the submit button
    submitBtn.disabled = true;
  
    // Hide the submit button and show the loading spinner
    submitBtn.style.display = 'none';
    loadingSpinner.style.display = 'block';
    myForm.submit();
    // wait for 1 second after submitting the form before enabling the submit button
    setTimeout(function() {
      console.log('waiting 1 second')
    }, 1000);
  
    document.addEventListener('DOMContentLoaded', function() {
      // Page content is loaded, and the loading indicator may have been removed
      submitBtn.disabled = false;
      submitBtn.style.display = 'block';
      loadingSpinner.style.display = 'none';
    }); 
  }
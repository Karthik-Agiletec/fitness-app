$(document).ready(function () {
  $("#detectDiseaseForm").submit(function (event) {
    event.preventDefault();
    var formData = new FormData(this);
    showConfirmation("Are you sure you want to detect the disease?", () => {
      DetectDisease(formData);
    });
  });
  $("#detectFormDisease").submit(function (event) {
    event.preventDefault();
    var formData = new FormData(this);
    showConfirmation("Are you sure you want to detect the disease?", () => {
      DetectFormDisease(formData);
    });
  });

  $("#image").change(function () {
    $("#disease_name").text("");
    $("#details-block").empty();
    $(".info-block").hide();
    displayImage(this);
  });
});

const displayImage = (input) => {
  var previewImage = $("#previewImage")[0];

  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function (e) {
      previewImage.src = e.target.result;
    };

    reader.readAsDataURL(input.files[0]);
  }
};

const DetectDisease = (formData) => {
  showProcessingAlert("Please wait....", false);
  PostRequest(
    detectDiseaseApiUrl,
    formData,
    (response) => {
      closeProcessingAlert();
      if (response.status) {
        $("#disease_name").text(response.data);
      } else {
        showError(response.message);
      }
    },
    true
  );
};
const DetectFormDisease = (formData) => {
  showProcessingAlert("Please wait....", false);
  PostRequest(
    detectFormApiUrl,
    formData,
    (response) => {
      closeProcessingAlert();
      if (response.status) {
        showInfo(response.result);
        
      } else {
        showError(response.message);
      }
    },
    true
  );
};

$(document).ready(function () {
        $("input[name='bank']").click(function () {
            var checkedValue = $("input[name='bank']:checked").val();
            console.log(checkedValue);
            if (checkedValue == "1") {
                $("#collapseOne").collapse('show');
                $("#collapseTwo").collapse('hide');
                $("#collapseThree").collapse('hide');
                $("#collapseFour").collapse('hide');
            }
            if (checkedValue == "2") {
                $("#collapseOne").collapse('hide');
                $("#collapseTwo").collapse('show');
                $("#collapseThree").collapse('hide');
                $("#collapseFour").collapse('hide');
            }
            if (checkedValue == "3") {
                $("#collapseOne").collapse('hide');
                $("#collapseTwo").collapse('hide');
                $("#collapseThree").collapse('show');
                $("#collapseFour").collapse('hide');
            }
            if (checkedValue == "4") {
               $("#collapseOne").collapse('hide');
                $("#collapseTwo").collapse('hide');
                $("#collapseThree").collapse('hide');
                $("#collapseFour").collapse('show');
            }
            else {
                console.log("Oops.");
            }
        });
    });
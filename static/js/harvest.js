document.addEventListener("DOMContentLoaded", function () {

    /* =====================================================
       HARVEST MODAL
    ===================================================== */

    const modal = document.getElementById("addHarvestModal");

    if (modal) {

        modal.addEventListener("hidden.bs.modal", function () {

            const form = modal.querySelector("form");

            if (form) {
                form.reset();
            }

        });

    }


    /* =====================================================
       EXPECTED & ACTUAL DATE
    ===================================================== */

    const expectedDate =
        document.getElementById("expected_harvest_date");

    const actualDate =
        document.getElementById("actual_harvest_date");


    if (expectedDate && actualDate) {

        actualDate.addEventListener("change", function () {

            if (
                expectedDate.value &&
                actualDate.value &&
                actualDate.value < expectedDate.value
            ) {

                alert(
                    "Actual harvest date cannot be earlier than expected harvest date."
                );

                actualDate.value = "";

            }

        });

    }


    /* =====================================================
       QUANTITY VALIDATION
    ===================================================== */

    const quantity =
        document.getElementById("quantity");


    if (quantity) {

        quantity.addEventListener("input", function () {

            if (parseFloat(this.value) < 0) {

                this.value = "";

            }

        });

    }


    /* =====================================================
       STATUS
    ===================================================== */

    const status =
        document.getElementById("status");


    if (status && actualDate) {

        status.addEventListener("change", function () {

            if (this.value === "Completed") {

                actualDate.required = true;

            } else {

                actualDate.required = false;

            }

        });

    }


    /* =====================================================
       TODAY DATE
    ===================================================== */

    const today = new Date();

    const year = today.getFullYear();

    const month =
        String(today.getMonth() + 1).padStart(2, "0");

    const day =
        String(today.getDate()).padStart(2, "0");

    const todayString =
        `${year}-${month}-${day}`;


    if (expectedDate) {
        expectedDate.min = todayString;
    }

    if (actualDate) {
        actualDate.min = todayString;
    }

});
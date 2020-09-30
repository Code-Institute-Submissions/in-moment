// Script allowing users to sort shop items by criteria.
$(() => {
    $("#sort").change(() => {
        /*
            Getting current url and value from select element on page.
            Splitting value of a selector to sort and direction.
            Changing url paramas according to selector values.
        */
        const selector = $("#sort");
        let currentUrl = new URL(window.location);

        let selectedVal = selector.val();

        if (selectedVal != "reset") {
            let sort = selectedVal.split("_")[0];
            let direction = selectedVal.split("_")[1];

            currentUrl.searchParams.set("sort", sort);
            currentUrl.searchParams.set("direction", direction);

            window.location.replace(currentUrl);
        } else {
            currentUrl.searchParams.delete("sort");
            currentUrl.searchParams.delete("direction");

            window.location.replace(currentUrl);
        }
    })
});
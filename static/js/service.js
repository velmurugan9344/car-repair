document.addEventListener("DOMContentLoaded", function () {
    console.log("✅ service.js is running!");

    document.querySelectorAll('.footer-service-link').forEach(link => {
        link.addEventListener('click', function (event) {
            event.preventDefault();
            var targetHash = this.getAttribute("href").split("#")[1];
            console.log(`🔗 Clicked on: ${targetHash}`);

            if (!targetHash) return;

            var targetSection = document.getElementById(targetHash);
            if (targetSection) {
                console.log(`✅ Found target: #${targetHash}`);

                // Check if this section is inside a Bootstrap tab
                var tabTrigger = document.querySelector(`[data-bs-target="#${targetHash}"]`);
                if (tabTrigger) {
                    var tab = new bootstrap.Tab(tabTrigger);
                    tab.show();
                    console.log(`✅ Activated tab for: #${targetHash}`);

                    // Wait for Bootstrap tab transition, then scroll
                    setTimeout(() => {
                        document.getElementById(targetHash).scrollIntoView({ behavior: "smooth", block: "start" });
                        console.log(`✅ Scrolled to: #${targetHash}`);
                    }, 300);
                } else {
                    // Directly scroll if no tab is involved
                    targetSection.scrollIntoView({ behavior: "smooth", block: "start" });
                    console.log(`✅ Directly scrolled to: #${targetHash}`);
                }

                // Update URL without reloading the page
                history.pushState(null, null, `#${targetHash}`);
            } else {
                console.warn(`❌ Element not found: #${targetHash}`);
            }
        });
    });
});

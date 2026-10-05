// Interactive client-side enhancements for Student Mental Health Analytics

document.addEventListener('DOMContentLoaded', () => {
    console.log("Student Mental Health Analytics Platform Initialized");

    // Responsive iframe scaling for Tableau
    const tableauFrame = document.getElementById('tableauIframe');
    if (tableauFrame) {
        function adjustIframeHeight() {
            const width = tableauFrame.clientWidth;
            if (width < 768) {
                tableauFrame.style.height = '650px';
            } else if (width < 1200) {
                tableauFrame.style.height = '850px';
            } else {
                tableauFrame.style.height = '1050px';
            }
        }
        window.addEventListener('resize', adjustIframeHeight);
        adjustIframeHeight();
    }
});

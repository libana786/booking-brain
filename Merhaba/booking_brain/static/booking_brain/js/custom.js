document.addEventListener("DOMContentLoaded", function () {
    // Your code here, including the code that uses jsPDF
        // Function to generate and download the PDF
        function generatePDFW() {
            const doc = new jsPDF('l','pt','letter');
            const table = document.getElementById("weekly");
            if(!table) {
                console.log("the table id is not fount")
            }

            doc.autoTable({
                html:'#weekly',
            }

            )
    
            // Save the PDF
            doc.save("weekly.pdf");
        }
        // monthly
        function generatePDFM() {
            const doc = new jsPDF('l','pt','letter');
            const table = document.getElementById("monthly");
            if(!table) {
                console.log("the table id is not fount")
            }

            doc.autoTable({
                html:'#monthly',
            }

            )
    
            // Save the PDF
            doc.save("monthly.pdf");
        }
        // today
        function generatePDFD() {
            const doc = new jsPDF('l','pt','letter');
            const table = document.getElementById("daily");
            if(!table) {
                console.log("the table id is not fount")
            }

            doc.autoTable({
                html:'#daily',
            }

            )
    
            // Save the PDF
            doc.save("daily.pdf");
        }

        function generatePDFC() {
            const doc = new jsPDF('l','pt','letter');
            const table = document.getElementById("custom");
            if(!table) {
                console.log("the table id is not fount")
            }

            doc.autoTable({
                html:'#custom',
            }

            )
    
            // Save the PDF
            doc.save("custom.pdf");
        }

        function generatePDFS() {
            const doc = new jsPDF('p','pt','letter');
            const table = document.getElementById("singleTable");
            if(!table) {
                console.log("the table id is not fount")
            }
            const logoImage = ''; 

            // Add the logo
            doc.addImage(logoImage, 'PNG', 40, 40, 100, 40); 

            doc.autoTable({
                html:'#singleTable',
            })
            const yPosition = doc.autoTable.previous.finalY + 20; // Adjust the vertical position as needed
            doc.setDrawColor(0); // Set line color to black
            doc.setLineWidth(1); // Set line width
            doc.line(40, yPosition, 550, yPosition); // Draw a horizontal line
            doc.autoTable({
                html:'#singleTable',
            })
            // Save the PDF
            doc.save("receipt.pdf");
        }
    
        // Add click event listener to the download button
        const todayButton = document.getElementById("todayButton");
        if (todayButton){
            todayButton.addEventListener("click", generatePDFD);
        }

        const weekButton = document.getElementById("weekButton");
        if (weekButton){
            weekButton.addEventListener("click", generatePDFW);
        }

        const monthButton = document.getElementById("monthButton");
        if (monthButton){
            monthButton.addEventListener("click", generatePDFM);
        }

        const singleButton = document.getElementById("singleButton");
        if (singleButton){
            singleButton.addEventListener("click", generatePDFS);
        }

        const customButton = document.getElementById("customButton");
        if (customButton){
            customButton.addEventListener("click", generatePDFC);
        }

        // make feilds reflect input add input event listener to the input field
            // Get references to the input fields
    const amountEAInput = document.getElementById("Amount_EA");
    const amountMComInput = document.getElementById("Amount_M_com");
    const amountZComInput = document.getElementById("Amount_Z_com");
    const amountTotalInput = document.getElementById("Amount");

    // Function to calculate and update the total amount
    function updateTotalAmount() {
        const amountEA = parseInt(amountEAInput.value) || 0;
        const amountMCom = parseInt(amountMComInput.value) || 0;
        const amountZCom = parseInt(amountZComInput.value) || 0;

        const totalAmount = amountEA + amountMCom + amountZCom;
        amountTotalInput.value = totalAmount; // Update the total amount without decimals
    }

    // Add event listeners to input fields to trigger the update
    amountEAInput.addEventListener("input", updateTotalAmount);
    amountMComInput.addEventListener("input", updateTotalAmount);
    amountZComInput.addEventListener("input", updateTotalAmount);

    // Initial calculation
    updateTotalAmount();

});


/**
 * DDoS Attack Detection and Mitigation - Main JavaScript
 */

document.addEventListener('DOMContentLoaded', function() {
    
    // Enable tooltips everywhere
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    });

    // Auto-dismiss alerts after 4 seconds
    setTimeout(function() {
        var alerts = document.querySelectorAll('.alert:not(.alert-permanent)')
        alerts.forEach(function(alert) {
            var alertInstance = new bootstrap.Alert(alert);
            alertInstance.close();
        });
    }, 4000);
    
    // Add active class to nav links based on current page
    const currentLocation = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        // Get the href attribute
        const linkPath = link.getAttribute('href');
        
        // Check if the current location matches the link's href
        if (linkPath === currentLocation) {
            link.classList.add('active');
            
            // If there's a parent li.nav-item, add active class to it as well
            const parentLi = link.closest('li.nav-item');
            if (parentLi) {
                parentLi.classList.add('active');
            }
        }
    });
    
    // Smooth scroll to anchors on documentation page
    if (currentLocation.includes('documentation')) {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                
                // Get the target element
                const targetId = this.getAttribute('href');
                const targetElement = document.querySelector(targetId);
                
                if (targetElement) {
                    // Smooth scroll to target
                    window.scrollTo({
                        top: targetElement.offsetTop - 20,
                        behavior: 'smooth'
                    });
                    
                    // Update URL
                    history.pushState(null, null, targetId);
                }
            });
        });
        
        // Highlight active section in documentation sidebar
        window.addEventListener('scroll', function() {
            const sections = document.querySelectorAll('.card[id]');
            const navItems = document.querySelectorAll('.list-group-item');
            
            let currentSection = '';
            
            sections.forEach(section => {
                const sectionTop = section.offsetTop;
                const sectionHeight = section.clientHeight;
                
                if (pageYOffset >= sectionTop - 100) {
                    currentSection = section.getAttribute('id');
                }
            });
            
            navItems.forEach(item => {
                item.classList.remove('active');
                if (item.getAttribute('href') === '#' + currentSection) {
                    item.classList.add('active');
                }
            });
        });
    }
    
    // Handle progress bars animation
    const progressBars = document.querySelectorAll('.progress-bar');
    if (progressBars.length > 0) {
        progressBars.forEach(bar => {
            const width = bar.style.width;
            
            // Set initial width to 0
            bar.style.width = '0%';
            
            // Animate to actual width
            setTimeout(() => {
                bar.style.width = width;
            }, 100);
        });
    }
    
    // Handle print functionality
    const printButtons = document.querySelectorAll('.btn-print');
    if (printButtons.length > 0) {
        printButtons.forEach(button => {
            button.addEventListener('click', function() {
                window.print();
            });
        });
    }
    
    // Handle form validation
    const forms = document.querySelectorAll('.needs-validation');
    if (forms.length > 0) {
        Array.from(forms).forEach(form => {
            form.addEventListener('submit', event => {
                if (!form.checkValidity()) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                
                form.classList.add('was-validated');
            }, false);
        });
    }
});

/**
 * Formats a number with commas as thousands separators
 * @param {number} number - The number to format
 * @return {string} The formatted number
 */
function formatNumber(number) {
    return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

/**
 * Creates a CSV download from table data
 * @param {string} tableId - The ID of the table to export
 * @param {string} filename - The filename for the CSV file
 */
function exportTableToCSV(tableId, filename = 'data.csv') {
    const table = document.getElementById(tableId);
    let csv = [];
    
    // Get all rows
    const rows = table.querySelectorAll('tr');
    
    for (let i = 0; i < rows.length; i++) {
        const row = [], cols = rows[i].querySelectorAll('td, th');
        
        for (let j = 0; j < cols.length; j++) {
            // Clean and quote the text content
            let data = cols[j].innerText.replace(/(\r\n|\n|\r)/gm, '').replace(/"/g, '""');
            row.push('"' + data + '"');
        }
        
        csv.push(row.join(','));
    }
    
    // Create CSV content
    const csvContent = 'data:text/csv;charset=utf-8,' + csv.join('\n');
    
    // Create download link
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement('a');
    link.setAttribute('href', encodedUri);
    link.setAttribute('download', filename);
    document.body.appendChild(link);
    
    // Trigger download
    link.click();
    document.body.removeChild(link);
}
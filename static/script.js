const socket = io();  // Initialize Socket.IO client

document.getElementById('setIpBtn').addEventListener('click', () => {
    const ip = document.getElementById('ipAddress').value;

    // Send the IP address to the server via Socket.IO
    if (validateIp(ip)) {
        socket.emit('set_ip', { ip: ip });
    } else {
        alert('Please enter a valid IP address.');
    }
});

const buttons = document.querySelectorAll('.action-btn');
buttons.forEach(button => {
    button.addEventListener('click', () => {
        const buttonNumber = button.innerText;  // Get the button number (1, 2, 3, or 4)
        
        // Toggle the clicked button
        if (button.classList.contains('active')) {
            button.classList.remove('active');  // Unpress the button if already active
        } else {
            // Unpress all other buttons
            buttons.forEach(btn => btn.classList.remove('active'));
            
            // Press the clicked button
            button.classList.add('active');
            
            // Emit the button click signal with the number
            socket.emit('button_click', { button: buttonNumber });
        }
    });
});

// Function to validate IP address format
function validateIp(ip) {
    const regex = /^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/;
    return regex.test(ip);
}

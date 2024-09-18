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
        socket.emit('button_click', { button: buttonNumber });  // Emit the button click signal with the number
    });
});

// Function to validate IP address format
function validateIp(ip) {
    const regex = /^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/;
    return regex.test(ip);
}

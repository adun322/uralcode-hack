import React from 'react';

function Footer() {
    return (
        <footer style={styles.footer}>
            <p>&copy; Купил мужик шляпу, а она ему как раз</p>
        </footer>
    );
}

const styles = {
    footer: {
        backgroundColor: '#444444',
        color: 'white',
        textAlign: 'center',
        verticalAlign : 'top',
        // lineHeight: '0px',
        padding: '0px',
        width: '100%',
        boxSizing: 'border-box',
        position: 'fixed',
        bottom: 0,
        left: 0,
        zIndex: 1000,
        height: '50px', // Фиксируем высоту футера
    },
};

export default Footer;

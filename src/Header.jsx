import React from 'react';

function Header() {
    return (
        <header style={styles.header}>
            <img src={"src/assets/2.png"} width={50} height={50}/>
            <h1 style={styles.title}>AI Assistant</h1>
        </header>
    );
}

const styles = {
    header: {
        backgroundColor: '#444444',
        color: 'white',
        textAlign: 'center',
        width: '100%',
        padding: '10px 20px',
        boxSizing: 'border-box',
        position: 'fixed',
        top: 0,
        left: 0,
        zIndex: 1000,
        height: '70px',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
    },
    title: {
        margin: 0,
        fontSize: '24px',
    },
    navList: {
        listStyleType: 'none',
        padding: 0,
        margin: 0,
        display: 'flex',
        gap: '20px',
    },
    navItem: {
        color: 'white',
        textDecoration: 'none',
        fontSize: '18px',
    },
};

export default Header;

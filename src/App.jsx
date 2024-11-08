import React from 'react';
import FileUploader from './FileUploader';
import Header from './Header';
import Footer from './Footer';

function App() {
    return (
        <div style={styles.appContainer}>
            <Header/>

            <FileUploader/>

            <Footer/>
        </div>
    );
}

const styles = {
};

export default App;

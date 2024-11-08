import React, { useState } from 'react';

function FileUploader() {
    const [selectedFile, setSelectedFile] = useState(null);
    const [uploading, setUploading] = useState(false);
    const [responseData, setResponseData] = useState(null);
    const [error, setError] = useState(null);
    const [showMessage, setShowMessage] = useState(true);

    const handleFileChange = (event) => {
        const file = event.target.files[0];
        if (file && file.size > 5 * 1024 * 1024) {
            setError('Размер файла превышает 5 МБ');
            setSelectedFile(null);
        } else {
            setSelectedFile(file);
            setError(null);
        }
    };

    const handleUpload = async () => {
        if (!selectedFile) return;

        setUploading(true);
        const formData = new FormData();
        formData.append('file', selectedFile);

        try {
            const response = await fetch('http://192.168.53.28:8000/file/upload-file', {
                method: 'POST',
                body: formData,
            });
            if (!response.ok) throw new Error('Ошибка сети');
            const data = await response.json();
            setResponseData(data);
            setError(null);
            setShowMessage(false);
        } catch (error) {
            console.error('Ошибка загрузки файла:', error);
            setError('Не удалось загрузить файл. Попробуйте снова.');
        } finally {
            setUploading(false);
        }
    };

    return (
            <div style={styles.s}>
                {showMessage && <h2>Выберите файл для проверки</h2>} {}
                <input type="file" onChange={handleFileChange}/>
                {error && <p style={styles.errorText}>{error}</p>}

                <button onClick={handleUpload} disabled={!selectedFile || uploading}>
                    {uploading ? 'Загрузка...' : 'Загрузить файл'}
                </button>

                {responseData && (
                    <div>
                        {Object.entries(responseData).map(([key, value]) => (
                            <div key={key} >
                                <h3>{key}</h3>
                                <p>{value}</p>
                            </div>
                        ))}
                    </div>
                )}
            </div>
    );
}

const styles = {
    s: {
        marginTop: '20px',
        marginBottom: '60px',
        marginLeft: '100px'
    }
};

export default FileUploader;

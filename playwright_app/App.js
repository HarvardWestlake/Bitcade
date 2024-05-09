import React, { useState } from 'react';
import ReactDOM from 'react-dom';

function App() {
    const [count, setCount] = useState(0);

    return (
        <div>
            <h1>Hello, React!</h1>
            <p>Current count: {count}</p>
            <button onClick={() => setCount(count + 1)} id="increment-button">
                Increment
            </button>
        </div>
    );
}

ReactDOM.render(<App />, document.getElementById('root'));

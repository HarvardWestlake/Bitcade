import React, { useState } from 'react';

const ListGames = () => {
    const [showMoreDescription, setShowMoreDescription] = useState(false);

    const toggleDescription = () => {
        setShowMoreDescription(!showMoreDescription);
    };

    return (
        <div className="list-games">
            <h3>Example Game</h3>
            <button onClick={toggleDescription}>Get Description</button>
            {showMoreDescription && (
                <div className="more-description" style={{ maxHeight: '200px', overflowY: 'auto' }}>
                    {/* Your detailed description content goes here */}
                </div>
            )}
        </div>
    );
};

export default ListGames;
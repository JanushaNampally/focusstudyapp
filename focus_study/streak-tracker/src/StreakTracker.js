import React, { userState, userEffect} from 'react';

const StreakTracker = () => {
    const [streak, setStreak] = useState(0);
    const [quote, setQuote] = useState("");

    useEffect(() => {
        fetch('/api/get_streak')
           .then(response => response.json())
           .then(data => setStreak(data.streak));
        
           fetch('https://api.quotable.io/random')
             .then(response => response.json())
             .then(data => setQuote(data.content));
    }, []);

    return (
        <div>
            <h3>Your Streak: {streak}</h3>
            <p>Motivation Quote : "{quote}"</p>
        </div>
    );
}

export default StreakTracker;
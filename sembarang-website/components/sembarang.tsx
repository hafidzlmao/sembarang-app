import React from "react";

const Sembarang: React.FC = () => {

    const [prompt, setPrompt] = React.useState("");

    const ENDPOINT: string = "https://ih47b84bgf.execute-api.ap-southeast-1.amazonaws.com/prod/generate_snippet_and_keywords"

    const onSubmission = () => {
        console.log("Submitting: " + prompt);
        fetch(`${ENDPOINT}?prompt=${prompt}`)
        .then((res)=> res.json())
        .then(console.log);
    };

    return (
        <>
            <h1>Sembarang</h1>
            <p>What is your brand about? Please let me know and I will generate a Nice blablabla and Keywords for your Product!</p>
            <input  type="text" 
                    placeholder="beef burger"
                    value={prompt}
                    onChange={(e) => setPrompt(e.currentTarget.value)}/>
            <button onClick={onSubmission}>Submit!</button>
        </>
    );
};

export default Sembarang;
import React, { useState } from "react"
import "./App.css"

export default function App() {
    const [result, setResult] = useState("")

    // handle click
    const handleClick = (e) => {
        setResult(result.concat(e.target?.name))
    }

    // handle clear
    const clear = () => {
        setResult("")
    }

    // handle backspace
    const backspace = () => {
        setResult(result?.slice(0, -1))
    }

    // handle the final calculation
    const calc = () => {
        const requestOptions = {
            headers: { "Content-Type": "application/json" },
            method: "POST",
            body: JSON.stringify({
                expr: result.toString()
            }),
        }

        fetch("/ ", requestOptions)
            .then(res => res.json())
            .then(json => {
                setResult(json.result.toString())
                console.log('fetch from flask', result)
            })
            .catch(error => {
                console.error(error);
            })
    }

    return (
        <div className="container">
            <h1 className="title">Calculator</h1>
            <div className="calculator">
                <input type="text" className="calc-numbers" value={result} disabled={true}/>
                <div className="calculator-buttons">
                    <button onClick={handleClick} name='(' className="btn purple">(</button>
                    <button onClick={handleClick} name=")" className="btn purple">)</button>
                    <button onClick={backspace} className="btn purple">&larr;</button>
                    <button onClick={clear} className="btn purple">C</button>
                    <button onClick={handleClick} name="7" className="btn">7</button>
                    <button onClick={handleClick} name="8" className="btn">8</button>
                    <button onClick={handleClick} name="9" className="btn">9</button>
                    <button onClick={handleClick} name="/" className="btn purple">&divide;</button>
                    <button onClick={handleClick} name="4" className="btn">4</button>
                    <button onClick={handleClick} name="5" className="btn">5</button>
                    <button onClick={handleClick} name="6" className="btn">6</button>
                    <button onClick={handleClick} name="*" className="btn purple">x</button>
                    <button onClick={handleClick} name="1" className="btn">1</button>
                    <button onClick={handleClick} name="2" className="btn">2</button>
                    <button onClick={handleClick} name="3" className="btn">3</button>
                    <button onClick={handleClick} name="-" className="btn purple">-</button>
                    <button onClick={handleClick} name="0" className="btn">0</button>
                    <button onClick={calc} className="btn purple equal span-2">=</button>
                    <button onClick={handleClick} name="+" className="btn purple">+</button>
                </div>
            </div>
        </div>
    )
}

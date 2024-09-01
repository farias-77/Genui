import styled from "styled-components";

export const Container = styled.div`
    width: 80%;
    height: 100%;

    display: flex;
    justify-content: center;
    align-items: center;

    padding: 25px;
`;

export const GeneratedContent = styled.div`
    width: 40%;
    height: 100%;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    padding: 20px;
    background-color: #f6f8f9;
    border-radius: 10px;
`;

export const Header = styled.div`
    width: 100%;
    height: 15%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;

    > div:first-child {
        width: 100%;

        display: flex;
        justify-content: space-between;
        align-items: center;

        h1 {
            font-size: 1.7rem;
            font-weight: 500;
        }

        div {
            width: 50px;
            height: 50px;
            border-radius: 10px;

            background-color: #5d63f1;

            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;

            font-size: 1.4em;
            font-weight: 500;
            color: #fff;
            text-align: center;
        }

        span {
            font-size: 0.7rem !important;
        }
    }

    > div:last-child {
        width: 100%;

        display: flex;
        justify-content: flex-end;
        align-items: center;

        cursor: pointer;

        color: #c0bfbf;
        margin-bottom: 10px;

        > div {
            width: 25px;
            height: 25px;

            display: flex;
            justify-content: center;
            align-items: center;

            background-color: #fff;
            margin-left: 10px;
            border-radius: 50%;
        }

        svg {
            color: #000;
            font-size: 0.9rem;
        }
    }
`;

export const Suggestions = styled.div`
    width: 100%;
    height: 85%;

    overflow: hidden;

    > div:last-child {
        width: 100%;
        height: 100%;

        overflow-y: auto;
        padding-right: 20px;

        &::-webkit-scrollbar {
            width: 10px;
            cursor: move;
            margin-top: 10px; /* Push the scrollbar down by 10px */
            margin-right: -5px; /* Move the scrollbar slightly to the left to centralize it within the padding */
        }

        &::-webkit-scrollbar-thumb {
            background-color: #f0f0f0;
            border-radius: 10px;
            cursor: grab;
        }

        &::-webkit-scrollbar-track {
            background-color: #f6f8f9;
        }

        &::-webkit-scrollbar-thumb:hover {
            background-color: #e0e0e0;
        }

        &::-webkit-scrollbar-thumb:active {
            background-color: #d0d0d0;
            cursor: grabbing;
        }
    }
`;

export const Suggestion = styled.div`
    width: 100%;
    height: 150px;

    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: flex-start;

    background-color: #fff;
    padding: 20px;
    border-radius: 10px;

    opacity: ${(props) => (props.visible ? 1 : 0)};
    transform: ${(props) =>
        props.visible ? "translateY(0)" : "translateY(100px)"};
    transition: opacity 0.3s ease-out, transform 0.3s ease-out;

    h1 {
        font-size: 1.2rem;
        font-weight: 500;
        color: #000;

        margin-bottom: 8px;
    }

    > p {
        width: calc(100% - 45px);

        font-size: 0.9rem;
        letter-spacing: 0.6px;
        font-weight: 300;
        color: #000;
        text-align: justify;
    }

    //footer
    > div {
        width: 100%;
        height: 35px;

        display: flex;
        justify-content: flex-end;
        align-items: center;

        //arrow box
        > div {
            width: 35px;
            height: 35px;

            display: flex;
            justify-content: center;
            align-items: center;

            background-color: #fff;
            border: 2px solid #5d63f1;
            border-radius: 10px;

            margin-left: 10px;

            cursor: pointer;

            &:hover {
                background-color: #5d63f1;

                svg {
                    color: #fff;
                }
            }
        }

        p {
            color: #5d63f1;
        }

        svg {
            font-size: 1rem;
            color: #5d63f1;
        }
    }

    & + & {
        margin-top: 20px;
    }
`;

export const AccountSummary = styled.div`
    width: 60%;
    height: 100%;

    padding: 0 30px;
`;

export const Profile = styled.div`
    width: 100%;
    height: 50px;

    display: flex;
    justify-content: flex-end;
    align-items: center;

    opacity: ${(props) => (props.isVisible ? 1 : 0)};
    transform: ${(props) =>
        props.isVisible ? "translateY(0)" : "translateX(200px)"};
    transition: opacity 0.3s ease-out, transform 0.3s ease-out;

    h1 {
        font-size: 1.2rem;
        font-weight: 500;
        color: #000;
    }

    svg {
        font-size: 2rem;
        color: #000;
        margin-left: 10px;
        cursor: pointer;
    }
`;

export const Balance = styled.div`
    width: 100%;
    height: 20%;

    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: flex-start;

    opacity: ${(props) => (props.isVisible ? 1 : 0)};
    transform: ${(props) =>
        props.isVisible ? "translateY(0)" : "translateX(-200px)"};
    transition: opacity 0.3s ease-out, transform 0.3s ease-out;

    h1 {
        font-size: 1.2rem;
        font-weight: 500;
        color: #000;
    }

    > p {
        font-size: 1.7rem;
        font-weight: 500;
        color: #000;
    }

    > div {
        width: 100%;

        display: flex;
        justify-content: space-between;
        align-items: center;
    }
`;

export const DaySummary = styled.div`
    width: 100%;

    margin-top: 20px;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;

    opacity: ${(props) => (props.isVisible ? 1 : 0)};
    transform: ${(props) =>
        props.isVisible ? "translateY(0)" : "translateX(200px)"};
    transition: opacity 0.3s ease-out, transform 0.3s ease;

    h1 {
        font-size: 1.2rem;
        font-weight: 500;
        color: #000;

        margin-bottom: 10px;
    }

    > div {
        width: 100%;

        display: flex;
        justify-content: space-between;
        align-items: center;
    }
`;

export const Predictions = styled.div`
    width: 100%;
    height: 20%;
    margin-top: 10px;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;

    opacity: ${(props) => (props.isVisible ? 1 : 0)};
    transform: ${(props) =>
        props.isVisible ? "translateY(0)" : "translateX(-200px)"};
    transition: opacity 0.3s ease-out, transform 0.3s ease-out;

    h1 {
        font-size: 1.2rem;
        font-weight: 500;
        color: #000;
    }

    span {
        font-size: 0.8rem;
        font-weight: 300;
        color: #000;

        margin-top: 5px;
    }

    > div {
        width: 100%;

        margin-top: 15px;

        display: flex;
        justify-content: space-between;
        align-items: center;

        > div {
            width: 32%;

            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: flex-start;

            h2 {
                font-size: 1rem;
                font-weight: 500;
                color: #000;

                margin-bottom: 5px;
            }
        }
    }
`;

export const ChartData = styled.div`
    width: 100%;
    height: 30%;

    position: relative;

    margin-top: 20px;

    canvas {
        display: block;

        width: 100% !important;
        height: 100% !important;
    }
`;

export const GrayBox = styled.div`
    width: ${(props) => props.width || "100%"};
    height: ${(props) => props.height || "100%"};

    background-color: #f6f8f9;
    border-radius: 10px;
    padding: 20px;

    color: ${(props) => props.color || "#000"};

    display: ${(props) => props.display || "flex"};
    flex-direction: ${(props) => props.flexDirection || "row"};
    justify-content: space-between;
    align-items: ${(props) => props.alignItems || "center"};

    svg {
        transform: ${(props) => props.rotate || "rotate(0deg)"};
        margin-right: 10px;
    }

    p {
        font-size: 1rem;
        font-weight: 400;
    }

    h3:first-child {
        font-size: 0.7rem;
        font-weight: 500;
    }

    h3:last-child {
        font-size: 1.4rem;
        font-weight: 500;
    }
`;

export const StyledLoadingScreen = styled.div`
    width: 100%;
    height: 100%;

    display: ${(props) => (props.display ? "flex" : "none")};
    align-items: center;
    justify-content: center;

    position: fixed;
    top: 0;
    left: 0;

    background-color: rgba(0, 0, 0, 0.5);
    backdrop-filter: blur(3px);
`;

export const LoadingContent = styled.div`
    width: 300px;
    height: 350px;
    padding: 20px;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    background-color: #fff;
    border-radius: 10px;

    text-align: center;
`;

export const LoadingMessage = styled.div`
    margin-bottom: 20px;
    font-size: 16px;
    color: #333;
`;

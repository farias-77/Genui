import styled from "styled-components";

export const Container = styled.div`
    width: 20%;
    height: 100%;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background: #fff;

    img {
        width: 50%;
        height: auto;
        object-fit: contain;

        margin-top: 60px;
    }
`;

export const Menu = styled.div`
    width: 100%;
    height: 100%;

    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;

    padding-top: 100px;

    background-color: #fff;
`;

export const MenuItem = styled.div`
    width: 60%;
    height: 50px;

    display: flex;
    justify-content: flex-start;
    align-items: center;

    border-radius: 10px;
    padding: 0 5px;

    cursor: pointer;

    div {
        width: 35px;
        height: 35px;

        display: flex;
        justify-content: center;
        align-items: center;

        background-color: ${(props) =>
            props.selected ? "#5D63F1" : "transparent"};
        border-radius: 10px;
    }

    p {
        font-size: 18px;
        font-weight: 500;
        color: ${(props) => (props.selected ? "#5D63F1" : "#d9d9d9")};

        margin-left: 20px;
    }

    svg {
        color: ${(props) => (props.selected ? "#fff" : "#d9d9d9")};
    }

    &:hover {
        background-color: #f2f2f2;
    }

    & + & {
        margin-top: 5px;
    }
`;

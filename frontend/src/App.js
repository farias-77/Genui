import { RouterProvider } from "react-router-dom";
import { ToastContainer } from "react-toastify";

import "./styles/reset.css";
import "./styles/index.css";

import router from "./routes/router";

export default function NoAuthApp() {
    return (
        <>
            <ToastContainer />
            <RouterProvider router={router} />
        </>
    );
}

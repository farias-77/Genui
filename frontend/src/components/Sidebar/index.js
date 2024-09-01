import { Container, Menu, MenuItem } from "./styles";

import { FaHome } from "react-icons/fa";
import { LuLayoutDashboard } from "react-icons/lu";
import { TiFlowMerge } from "react-icons/ti";
import { PiWarningCircle, PiMoneyWavy } from "react-icons/pi";
import { TbTargetArrow } from "react-icons/tb";

import logo from "../../assets/genui_escuro.png";

export default function Sidebar() {
    return (
        <Container>
            <img src={logo} alt="Logo" />
            <Menu>
                <MenuItem selected={true}>
                    <div>
                        <FaHome size={24} />
                    </div>
                    <p>Início</p>
                </MenuItem>
                <MenuItem selected={false}>
                    <div>
                        <LuLayoutDashboard size={24} />
                    </div>
                    <p>Dashboard</p>
                </MenuItem>
                <MenuItem selected={false}>
                    <div>
                        <TiFlowMerge size={24} />
                    </div>
                    <p>Insights</p>
                </MenuItem>
                <MenuItem selected={false}>
                    <div>
                        <PiWarningCircle size={24} />
                    </div>
                    <p>Avisos</p>
                </MenuItem>
                <MenuItem selected={false}>
                    <div>
                        <TbTargetArrow size={24} />
                    </div>
                    <p>Metas e objetivos</p>
                </MenuItem>
                <MenuItem selected={false}>
                    <div>
                        <PiMoneyWavy size={24} />
                    </div>
                    <p>Transações</p>
                </MenuItem>
            </Menu>
        </Container>
    );
}

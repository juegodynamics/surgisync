import React from 'react';
import axios from 'axios';
import Stack from '@mui/material/Stack';
import Paper from '@mui/material/Paper';
import {ActionDrawer, DRAWER_WIDTH} from './ActionDrawer';
import Box from '@mui/material/Box';
import Drawer from '@mui/material/Drawer';
import CssBaseline from '@mui/material/CssBaseline';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import List from '@mui/material/List';
import Typography from '@mui/material/Typography';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';

import Divider from '@mui/material/Divider';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import InboxIcon from '@mui/icons-material/MoveToInbox';
import MailIcon from '@mui/icons-material/Mail';
import {Appointment} from 'models/Appointment';
import {AppointmentCard} from './AppointmentCard';

const SURGICAL_UUID = '328ddb8a-8229-4d7a-b2cf-30973b8cc85e';
const HOST = 'localhost:8000';
const getDefaultNewAppointment = (): Appointment => ({
    resourceType: 'Appointment',
    status: 'pending',
    subject: {
        reference: '22c7dbd1-8de4-b7c3-b2ed-63dded3aca23',
        type: 'Patient',
    },
    start: new Date(),
    end: new Date(),
    participant: [
        {
            actor: {reference: SURGICAL_UUID, type: 'Organization'},
            required: true,
            status: 'tentative',
            type: {
                text: 'attender',
                coding: [
                    {
                        system: 'http://terminology.hl7.org/CodeSystem/v3-ParticipationType',
                        code: 'ATND',
                        display: 'attender',
                    },
                ],
            },
        },
    ],
});

export default function SchedulingPage() {
    const [appointments, setAppointments] = React.useState<Array<Appointment>>(
        []
    );
    const [isLoading, setIsLoading] = React.useState<boolean>(true);
    const [selectedAppointment, setSelectedAppointment] = React.useState<
        number | null
    >(null);

    React.useEffect(() => {
        const fetchAppointments = async () => {
            setIsLoading(true);
            try {
                const {data: response} = await axios.get<Appointment[]>(
                    `http://${HOST}/v1/appointments/participant/${SURGICAL_UUID}`
                );
                setAppointments(response);
                if (response.length) {
                    setSelectedAppointment(0);
                }
            } catch (error: any) {
                console.error(error.message);
            }
            setIsLoading(false);
        };

        fetchAppointments();
    }, []);

    const onSaveAppointment = React.useCallback((appointment: Appointment) => {
        const postAppointment = async () => {
            setIsLoading(true);
            try {
                const {data: response} = await axios
                    .post<Appointment>(
                        `http://${HOST}/v1/appointments/${appointment.id}`,
                        appointment
                    )
                    .then(() =>
                        axios.get<Appointment[]>(
                            `http://${HOST}/v1/appointments/participant/${SURGICAL_UUID}`
                        )
                    );

                setAppointments(response);
            } catch (error: any) {
                console.error(error.message);
            }
            setIsLoading(false);
        };

        postAppointment();
    }, []);

    const onNewAppointment = React.useCallback(() => {
        const postAppointment = async () => {
            setIsLoading(true);

            try {
                const {data: response} = await axios
                    .post<Appointment>(
                        `http://${HOST}/v1/appointments`,
                        getDefaultNewAppointment()
                    )
                    .then(() =>
                        axios.get<Appointment[]>(
                            `http://${HOST}/v1/appointments/participant/${SURGICAL_UUID}`
                        )
                    );

                setAppointments(response);
            } catch (error: any) {
                console.error(error.message);
            }
            setIsLoading(false);
        };

        postAppointment();
    }, []);

    return (
        <Box sx={{display: 'flex'}}>
            <CssBaseline />
            <AppBar
                position="fixed"
                sx={{
                    width: `calc(100% - ${DRAWER_WIDTH}px)`,
                    ml: `${DRAWER_WIDTH}px`,
                }}
            >
                <Toolbar>
                    <Typography variant="h6" noWrap component="div">
                        Surgisync
                    </Typography>
                </Toolbar>
            </AppBar>
            <ActionDrawer
                selectedAppointment={selectedAppointment}
                appointments={appointments}
                onNewAppointment={onNewAppointment}
            />
            <Box
                component="main"
                sx={{flexGrow: 1, bgcolor: 'background.default', p: 3}}
            >
                <Toolbar />
                {isLoading ? (
                    <Typography>{'Loading'}</Typography>
                ) : selectedAppointment !== null ? (
                    <AppointmentCard
                        appointment={appointments[selectedAppointment]}
                    />
                ) : (
                    <Typography>{'Please select appointment'}</Typography>
                )}
            </Box>
        </Box>
    );
}

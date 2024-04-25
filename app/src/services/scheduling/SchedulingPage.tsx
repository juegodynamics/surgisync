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
import {Appointment, Patient} from 'models/Appointment';
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
            type: [
                {
                    text: 'attender',
                    coding: [
                        {
                            system: 'http://terminology.hl7.org/CodeSystem/v3-ParticipationType',
                            code: 'ATND',
                            display: 'attender',
                        },
                    ],
                },
            ],
        },
    ],
});

export const useSchedulingDataAPI = () => {
    const [appointments, setAppointments] = React.useState<Appointment[]>([]);
    const [patients, setPatients] = React.useState<Patient[]>([]);
    const [isLoading, setIsLoading] = React.useState<boolean>(true);

    React.useEffect(() => {
        const fetchData = async () => {
            setIsLoading(true);

            try {
                const [{data: appointmentsData}, {data: patientsData}] =
                    await Promise.all([
                        axios.get<Appointment[]>(
                            `http://${HOST}/v1/appointments/participant/${SURGICAL_UUID}`
                        ),
                        axios.get<Patient[]>(`http://${HOST}/v1/patients`),
                    ]);
                setAppointments(
                    appointmentsData.sort((a, b) =>
                        (a.id || '') > (b.id || '') ? -1 : 1
                    )
                );
                setPatients(
                    patientsData.sort((a, b) =>
                        (a.id || '') > (b.id || '') ? -1 : 1
                    )
                );
            } catch (error: any) {
                console.error(error.message);
            }
            setIsLoading(false);
        };

        fetchData();
    }, []);

    const onSaveAppointment = React.useCallback((appointment: Appointment) => {
        const postAppointment = async () => {
            setIsLoading(true);
            try {
                const {data: appointmentsData} = await axios
                    .post<Appointment>(
                        `http://${HOST}/v1/appointments/${appointment.id}`,
                        appointment
                    )
                    .then(() =>
                        axios.get<Appointment[]>(
                            `http://${HOST}/v1/appointments/participant/${SURGICAL_UUID}`
                        )
                    );

                setAppointments(
                    appointmentsData.sort((a, b) =>
                        (a.id || '') > (b.id || '') ? -1 : 1
                    )
                );
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

            const appointment = getDefaultNewAppointment();

            try {
                const {data: appointmentsData} = await axios
                    .post<Appointment>(
                        `http://${HOST}/v1/appointments/`,
                        appointment
                    )
                    .then(() =>
                        axios.get<Appointment[]>(
                            `http://${HOST}/v1/appointments/participant/${SURGICAL_UUID}`
                        )
                    );

                setAppointments(
                    appointmentsData.sort((a, b) =>
                        (a.id || '') > (b.id || '') ? -1 : 1
                    )
                );
            } catch (error: any) {
                console.error(error);
            }
            setIsLoading(false);
        };

        postAppointment();
    }, []);

    const onDeleteAppointment = React.useCallback((appointmentId: string) => {
        const deleteAppointment = async () => {
            setIsLoading(true);

            try {
                const {data: appointmentsData} = await axios
                    .delete<Appointment>(
                        `http://${HOST}/v1/appointments/${appointmentId}`
                    )
                    .then(() =>
                        axios.get<Appointment[]>(
                            `http://${HOST}/v1/appointments/participant/${SURGICAL_UUID}`
                        )
                    );

                setAppointments(
                    appointmentsData.sort((a, b) =>
                        (a.id || '') > (b.id || '') ? -1 : 1
                    )
                );
            } catch (error: any) {
                console.error(error);
            }
            setIsLoading(false);
        };

        deleteAppointment();
    }, []);

    return {
        appointments,
        setAppointments,
        patients,
        setPatients,
        isLoading,
        setIsLoading,
        onSaveAppointment,
        onNewAppointment,
        onDeleteAppointment,
    };
};

export default function SchedulingPage() {
    // const [appointments, setAppointments] = React.useState<Array<Appointment>>(
    //     []
    // );
    // const [patients, setPatients] = React.useState<Array<Appointment>>(
    //     []
    // );
    // const [isLoading, setIsLoading] = React.useState<boolean>(true);
    const {
        appointments,
        setAppointments,
        patients,
        setPatients,
        isLoading,
        setIsLoading,
        onSaveAppointment,
        onNewAppointment,
        onDeleteAppointment,
    } = useSchedulingDataAPI();

    const [selectedAppointment, setSelectedAppointment] = React.useState<
        number | null
    >(null);

    React.useEffect(() => {
        if (!isLoading && selectedAppointment === null && appointments.length) {
            setSelectedAppointment(0);
        }
    }, [isLoading, selectedAppointment, appointments.length]);

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
                setSelectedAppointment={setSelectedAppointment}
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
                        patients={patients}
                        appointment={appointments[selectedAppointment]}
                        updateAppointment={(appointment) =>
                            setAppointments([
                                ...appointments.slice(0, selectedAppointment),
                                appointment,
                                ...appointments.slice(
                                    selectedAppointment + 1,
                                    appointments.length
                                ),
                            ])
                        }
                        saveAppointment={onSaveAppointment}
                        deleteAppointment={onDeleteAppointment}
                    />
                ) : (
                    <Typography>{'Please select appointment'}</Typography>
                )}
            </Box>
        </Box>
    );
}

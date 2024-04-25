import React from 'react';
import axios from 'axios';
import dayjs from 'dayjs';
import Stack from '@mui/material/Stack';
import Paper from '@mui/material/Paper';
import {ActionDrawer, DRAWER_WIDTH} from './ActionDrawer';
import Box from '@mui/material/Box';
import Drawer from '@mui/material/Drawer';
import CssBaseline from '@mui/material/CssBaseline';
import AppBar from '@mui/material/AppBar';
import Select from '@mui/material/Select';
import Toolbar from '@mui/material/Toolbar';
import List from '@mui/material/List';
import Typography from '@mui/material/Typography';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import {DemoContainer, DemoItem} from '@mui/x-date-pickers/internals/demo';
import {AdapterDayjs} from '@mui/x-date-pickers/AdapterDayjs';
import {LocalizationProvider} from '@mui/x-date-pickers/LocalizationProvider';
import {DateField} from '@mui/x-date-pickers/DateField';
import {TimeField} from '@mui/x-date-pickers/TimeField';
import {DateTimeField} from '@mui/x-date-pickers/DateTimeField';
import {Appointment} from 'models/Appointment';

export const AppointmentCard = ({appointment}: {appointment: Appointment}) => {
    return (
        <LocalizationProvider dateAdapter={AdapterDayjs}>
            <Card>
                <CardContent>
                    <Stack spacing={2}>
                        <Typography variant="h2">{`Appointment ${
                            appointment.id || '(unsaved)'
                        }`}</Typography>

                        <DemoItem label="Start Date Time">
                            <DateTimeField
                                value={dayjs(appointment.start)}
                                defaultValue={dayjs('2022-04-17T15:30')}
                            />
                        </DemoItem>
                        <DemoItem label="End Date Time">
                            <DateTimeField
                                value={dayjs(appointment.end)}
                                defaultValue={dayjs('2022-04-17T15:30')}
                            />
                        </DemoItem>
                    </Stack>
                </CardContent>
            </Card>
        </LocalizationProvider>
    );
};

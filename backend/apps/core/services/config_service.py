from django.db import IntegrityError, transaction

from apps.core.models import AcademicPeriod, SpaceType, TimeSlot, WorkingDay


class ConfigServiceError(Exception):
    pass


class ConfigValidationError(ConfigServiceError):
    pass


def _normalize_name(name):
    return (name or "").strip()


def _validate_period(start_date, end_date):
    if start_date > end_date:
        raise ConfigValidationError(
            "La fecha de fin debe ser mayor o igual a la fecha de inicio."
        )


def _validate_day_of_week(day_of_week):
    if day_of_week < 1 or day_of_week > 7:
        raise ConfigValidationError("El dia laborable debe estar entre 1 y 7.")


def _validate_time_range(start_time, end_time):
    if start_time >= end_time:
        raise ConfigValidationError("La hora de fin debe ser mayor a la hora de inicio.")


@transaction.atomic
def create_academic_period(*, code, name, start_date, end_date, is_active=True):
    _validate_period(start_date, end_date)

    try:
        return AcademicPeriod.objects.create(
            code=code.strip(),
            name=_normalize_name(name),
            start_date=start_date,
            end_date=end_date,
            is_active=is_active,
        )
    except IntegrityError as exc:
        raise ConfigValidationError("Ya existe un periodo con ese codigo.") from exc


@transaction.atomic
def update_academic_period(period, *, code, name, start_date, end_date, is_active):
    _validate_period(start_date, end_date)

    period.code = code.strip()
    period.name = _normalize_name(name)
    period.start_date = start_date
    period.end_date = end_date
    period.is_active = is_active

    try:
        period.save()
    except IntegrityError as exc:
        raise ConfigValidationError("Ya existe un periodo con ese codigo.") from exc

    return period


@transaction.atomic
def create_working_day(*, day_of_week, name, is_active=True):
    _validate_day_of_week(day_of_week)

    try:
        return WorkingDay.objects.create(
            day_of_week=day_of_week,
            name=_normalize_name(name),
            is_active=is_active,
        )
    except IntegrityError as exc:
        raise ConfigValidationError("Ya existe ese dia laborable.") from exc


@transaction.atomic
def update_working_day(working_day, *, day_of_week, name, is_active):
    _validate_day_of_week(day_of_week)

    working_day.day_of_week = day_of_week
    working_day.name = _normalize_name(name)
    working_day.is_active = is_active

    try:
        working_day.save()
    except IntegrityError as exc:
        raise ConfigValidationError("Ya existe ese dia laborable.") from exc

    return working_day


@transaction.atomic
def create_time_slot(*, name, start_time, end_time, is_active=True):
    _validate_time_range(start_time, end_time)

    try:
        return TimeSlot.objects.create(
            name=_normalize_name(name),
            start_time=start_time,
            end_time=end_time,
            is_active=is_active,
        )
    except IntegrityError as exc:
        raise ConfigValidationError("Ya existe una franja con ese nombre y horario.") from exc


@transaction.atomic
def update_time_slot(time_slot, *, name, start_time, end_time, is_active):
    _validate_time_range(start_time, end_time)

    time_slot.name = _normalize_name(name)
    time_slot.start_time = start_time
    time_slot.end_time = end_time
    time_slot.is_active = is_active

    try:
        time_slot.save()
    except IntegrityError as exc:
        raise ConfigValidationError("Ya existe una franja con ese nombre y horario.") from exc

    return time_slot


@transaction.atomic
def create_space_type(*, name, description="", is_active=True):
    try:
        return SpaceType.objects.create(
            name=_normalize_name(name),
            description=(description or "").strip(),
            is_active=is_active,
        )
    except IntegrityError as exc:
        raise ConfigValidationError("Ya existe un tipo de espacio con ese nombre.") from exc


@transaction.atomic
def update_space_type(space_type, *, name, description, is_active):
    space_type.name = _normalize_name(name)
    space_type.description = (description or "").strip()
    space_type.is_active = is_active

    try:
        space_type.save()
    except IntegrityError as exc:
        raise ConfigValidationError("Ya existe un tipo de espacio con ese nombre.") from exc

    return space_type

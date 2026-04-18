import { LoginPanel } from "./features/auth/components/LoginPanel";
import {
  RoleHomeView,
  SessionLoadingView,
} from "./features/auth/components/SessionStateView";
import { useAuthSession } from "./features/auth/hooks/useAuthSession";
import { SystemConfigPanel } from "./features/config/components/SystemConfigPanel";
import { useSystemConfig } from "./features/config/hooks/useSystemConfig";
import { UsersDashboard } from "./features/users/components/UsersDashboard";
import { useUsersManagement } from "./features/users/hooks/useUsersManagement";
import { coreApiBase } from "./shared/api/coreApiClient";

function App() {
  const {
    authToken,
    currentUser,
    authLoading,
    loginState,
    setLoginState,
    handleLogin,
    handleLogout,
  } = useAuthSession();

  const isAdmin = Boolean(authToken && currentUser?.role === "administrador");

  const {
    roles,
    users,
    usersLoading,
    usersError,
    formMode,
    formState,
    selectedUser,
    setFormState,
    loadUsersAndRoles,
    resetFormToCreate,
    handleSelectEdit,
    handleSubmitForm,
    handleDeactivateUser,
  } = useUsersManagement({
    authToken,
    enabled: isAdmin,
  });

  const {
    configState,
    refreshAll,
    handleFieldChange,
    handleSelectEdit: handleConfigSelectEdit,
    handleDelete,
    handleSubmit,
    resetResourceForm,
  } = useSystemConfig({
    authToken,
    enabled: isAdmin,
  });

  const handleFormChange = (field, value) => {
    setFormState((previous) => ({
      ...previous,
      [field]: value,
    }));
  };

  if (authLoading) {
    return <SessionLoadingView />;
  }

  if (!authToken) {
    return (
      <LoginPanel
        apiBaseLabel={coreApiBase}
        loginState={loginState}
        setLoginState={setLoginState}
        onSubmit={handleLogin}
      />
    );
  }

  if (!isAdmin) {
    return <RoleHomeView currentUser={currentUser} onLogout={handleLogout} />;
  }

  return (
    <main className="app-shell">
      <div className="admin-page-stack">
        <UsersDashboard
          currentUser={currentUser}
          formMode={formMode}
          formState={formState}
          roles={roles}
          selectedUser={selectedUser}
          users={users}
          usersLoading={usersLoading}
          usersError={usersError}
          onRefresh={loadUsersAndRoles}
          onLogout={handleLogout}
          onFormChange={handleFormChange}
          onFormSubmit={handleSubmitForm}
          onCancelEdit={resetFormToCreate}
          onSelectEdit={handleSelectEdit}
          onDeactivate={handleDeactivateUser}
        />

        <SystemConfigPanel
          configState={configState}
          onRefresh={refreshAll}
          onFieldChange={handleFieldChange}
          onSubmit={handleSubmit}
          onEdit={handleConfigSelectEdit}
          onDelete={handleDelete}
          onCancel={resetResourceForm}
        />
      </div>
    </main>
  );
}

export default App;
